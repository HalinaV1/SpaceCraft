class PID(object):
    def __init__(self, KP, KI, KD):
        self.kp = KP
        self.ki = KI
        self.kd = KD
        self.ki_thr = 20      # threshold, m
        self.p_error = 0
        self.p_error_last = 0
        self.i_error = 0
        self.d_error = 0
        self.output = 0
       
    def copmpute(self, input, setpoint, time_delta):
        self.p_error = setpoint - input
        
        if -self.ki_thr < self.p_error < self.ki_thr:
            self.i_error += self.p_error * time_delta
        else:
            self.i_error = 0
            
        self.d_error = (self.p_error - self.p_error_last) / time_delta
        
        self.p_error_last = self.p_error

        output = (self.kp * self.p_error) + (self.ki * self.i_error) + (self.kd * self.d_error)
        
        self.output = min(max(output, 0), 100)
        return self.output
    
    def get_pp(self):
        return self.kp * self.p_error
    
    def get_pi(self):
        return self.ki * self.i_error
    
    def get_pd(self):
        return self.kd * self.d_error




