
from kfp import dsl
from kfp import compiler

@dsl.component
def hello_world():
    print("Hello World from Kubeflow Pipelines!")

@dsl.pipeline(
    name="hello-world-pipeline",
    description="My first Kubeflow pipeline"
)
def hello_pipeline():
    hello_world()

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=hello_pipeline,
        package_path="hello-world.yaml"
    )
