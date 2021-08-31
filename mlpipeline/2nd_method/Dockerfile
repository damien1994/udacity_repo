FROM continuumio/miniconda3

ARG WANDB_API_KEY=<API_KEY>
ENV WANDB_API_KEY $WANDB_API_KEY

RUN pip install mlflow==1.19.0 \
    && pip install wandb==0.12.0 \
    && pip install requests==2.24.0 \