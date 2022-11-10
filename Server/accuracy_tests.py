from model_run import predict
from generator import get_captcha_image
from time import sleep
from datetime import datetime
def test_accuracy(sample_size=100,text_size=4,digit_only=True,model_id=1,log_data=False):
    """
    generates sample_size captchas and tests the model's accuracy. can adjust the number of characters in the captcha and whether it contains english letters or just digits.
    model_id and log_data are used for logging purposes and aren't used by default
    model 1 was the first model trained in 1/11/2022
    """
    #counter for correct answers
    correct = 0
    for _ in range(sample_size):
        #create a captcha and predict its answer until sample_size is reached
        s = get_captcha_image(text_size,digit_only)
        if s == predict('out.png'):
            correct+=1
        
    #save accuracy
    accuracy = round(correct / sample_size,3) 
    #logging test results
    if log_data:
        digit_s = ''
        if digit_only:
            digit_s = "digits only"
        else:
            digit_s = "digits and small case english letters"
        #write test results and info on file
        f = open('ACCURACY_LOG.txt','a')
        f.write(f'''model id {model_id}\ntest done in {datetime.now().strftime("%d/%m/%Y %H:%M")}
type {digit_s}\nsample size {sample_size}\naccuracy {accuracy}\n''' + '-' * 20 +'\n') 

    
    return accuracy

