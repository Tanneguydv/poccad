FROM continuumio/miniconda

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "dev_pythonocc", "/bin/bash", "-c"]

ENV PATH /opt/conda/envs/dev_pythonocc/bin:$PATH

WORKDIR /app/pythonocc-demos

COPY core_webgl_threejs_torus.py .

EXPOSE 8000

ENTRYPOINT [ "python", "core_webgl_threejs_torus.py" ]

