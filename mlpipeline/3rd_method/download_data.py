import click
import logging
import pathlib
import mlflow
import requests
import tempfile

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def print_message(input):
    return f'Hello {input}'


@click.command(help="Hello world mlflow")
@click.option("--input", type=str, help="input word", required=True)
#@click.option("--artifact_name", type=str, help="Name for the artifact", required=True)
#@click.option("--artifact_type", type=str, help="Type for the artifact", required=True)
#@click.option("--artifact_description", type=str, help="Description for the artifact", required=True)
def go(input):
    # Derive the base name of the file from the URL
    #basename = pathlib.Path(file_url).name.split("?")[0].split("#")[0]

    # Download file, streaming so we can download files larger than
    # the available memory. We use a named temporary file that gets
    # destroyed at the end of the context, so we don't leave anything
    # behind and the file gets removed even in case of errors
    #logger.info(f"Downloading {file_url} ...")
    #with tempfile.NamedTemporaryFile(mode='wb+') as fp:

    logger.info("Creating run exercise_2")
    with mlflow.start_run(run_name='download_data_mlflow') as run:
        # get run id
        run_id = run.info.run_id
        # Download the file streaming and write to open temp file


        # Make sure the file has been written to disk before uploading
        # to W&B

        logger.info("Log params")
        mlflow.log_param('run_id', run_id)
        mlflow.log_param('input', input)
        #mlflow.log_param('artifact_description', artifact_description)

        #output = print_message(input)
        logger.info("Creating artifact")
        # Log an artifact (output file)
        with open("output.txt", "w") as f:
            f.write(print_message(input))
        mlflow.log_artifact("output.txt")
        #with tempfile.NamedTemporaryFile(mode='wb+') as fp:
        #    fp.write(output)
        #    fp.flush()
        #    mlflow.log_artifact(fp.name)


if __name__ == '__main__':
    go()
