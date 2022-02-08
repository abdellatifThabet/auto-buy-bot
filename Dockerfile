FROM python:3.7


#RUN set -xe \
#    && apt-get update -y \
#    && apt-get install libssl-dev libffi-dev -y \
#    && apt-get install python3.7 -y \
#    && apt-get install python-pip -y
RUN pip install --upgrade pip

RUN pip install selenium
RUN pip install webdriver_manager
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -y \
    && apt-get install google-chrome-stable -y



COPY . .
CMD apt-get autoclean
CMD python auto-buy-bot.py
