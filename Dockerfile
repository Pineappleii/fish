FROM fish-base

ENV PATH /usr/local/bin:$PATH
ADD . /fish
WORKDIR /fish

CMD python main.py