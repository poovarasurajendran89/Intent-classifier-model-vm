from kfp import dsl, compiler

@dsl.component
def data_ingestion():
    print("Ingesting data")

@dsl.component
def preprocessing():
    print("Preprocessing data")

@dsl.component
def model_training():
    print("Training model")

@dsl.component
def model_evaluation():
    print("Evaluating model")

@dsl.pipeline(name="mlops-dag-pipeline")
def mlops_pipeline():

    ingestion = data_ingestion()

    preprocess = preprocessing().after(ingestion)

    training = model_training().after(preprocess)

    evaluation = model_evaluation().after(training)

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=mlops_pipeline,
        package_path="mlops-pipeline.yaml"
    )