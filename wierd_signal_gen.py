import time
import math

def sine_wave_generator(frequency, amplitude=1.0):
    """
    Generates a continuous sine wave with given frequency, sample rate, and amplitude.
    :param frequency: Frequency of the sine wave in Hz
    :param sample_rate: Number of samples per second
    :param amplitude: Amplitude of the wave (0 to 1.0)
    """
                                             #
                           #                    
                                                                            #
                                                               #                                
                                                           #                       
                                                                #                                    
        
if __name__ == "__main__":
    frequency = float(input("Enter frequency in Hz: "))
    amplitude = float(input("Enter amplitude (0-1): "))
    transfromfactor = int(input("Enter the transofrming factor of the plane: "))
    #generator = sine_wave_generator(frequency, sample_rate, amplitude)
    t = 0  # Time index in seconds 
    try:
        while True:
            value = amplitude * math.sin(2 * math.pi * frequency)      #        this should be insude the promt loop
            
            #Wave plotting
            #bar_length = int(1+value*transfromfactor)# Scale the value to fit in a range of 0 to 20
            #bar = '+'*bar_length
            print(f"{value:.6f}")
            time.sleep(1/frequency)       
            
    except KeyboardInterrupt:
            print("Exiting...")
            exit(0) 