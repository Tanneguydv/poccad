FROM continuumio/miniconda3

RUN conda install nomkl
RUN conda install -c conda-forge -c dlr-sc -c tpaviot -c oce -c pythonocc pythonocc-core==0.18.2 python=3.7

ENTRYPOINT []
CMD [ "/bin/bash" ]