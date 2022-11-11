from model_run import predict
from generator import get_captcha_image
from datetime import datetime
from time import time

def format(sample_size,text_size,digit_only,model_id,accuracy, rate):
    """
    formats the test results to be more readable, writes the log on TESTS_LOG.txt
    """
    model_id_s = str(model_id)
    model_id_s += ' ' * (24 - len(model_id_s)) 

    type = ''
    if digit_only:
        type += "digits only"
    else:
        type += "digits and small case english letters"
    type += ' ' * (48 - len(type))

    date = datetime.now().strftime("%d/%m/%Y %H:%M") + ' ' * 8

    text_size_s = str(text_size)
    text_size_s += (16 - len(text_size_s)) * ' '

    sample_size_s = str(sample_size)
    sample_size_s += (24 - len(sample_size_s)) * ' '

    accuracy_s = str(accuracy * 100) + '%'
    accuracy_s += (24 - len(accuracy_s)) * ' '

    solve_rate_s = str(rate)
    solve_rate_s += (25 - len(solve_rate_s)) * ' ' + '\n'

    table = model_id_s + date + type + text_size_s + sample_size_s + accuracy_s + solve_rate_s
    line = len(table) * '-' + '\n'

    f= open('TESTS_LOG.TXT','a')
    f.write(table + line) 
    f.close()

def test_model(sample_size=100,text_size=4,digit_only=True,model_id=1,log_data=False):
    """
    generates sample_size captchas and tests the model's accuracy. can adjust the number of characters in the captcha and whether it contains english letters or just digits.
    model_id and log_data are used for logging purposes and aren't used by default
    model 1 was the first model trained in 1/11/2022
    """
    #counter for correct answers
    correct = 0
    runtime = time()
    for _ in range(sample_size):
        #create a captcha and predict its answer until sample_size is reached
        s = get_captcha_image(text_size,digit_only)
        if s == predict('out.png'):
            correct+=1
    #save speed
    solve_rate = round(sample_size / (time() - runtime),3)
    #save accuracy
    accuracy = round(correct / sample_size,3) 
    #logging test results
    if log_data:
        format(sample_size,text_size,digit_only,model_id,accuracy,solve_rate)
    
    return accuracy

