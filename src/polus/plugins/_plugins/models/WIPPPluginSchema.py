# generated by datamodel-codegen:
#   filename:  wipp-plugin-manifest-schema.json
#   timestamp: 2023-01-04T14:54:38+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, constr


class Type(Enum):
    collection = "collection"
    stitchingVector = "stitchingVector"
    tensorflowModel = "tensorflowModel"
    csvCollection = "csvCollection"
    pyramid = "pyramid"
    pyramidAnnotation = "pyramidAnnotation"
    notebook = "notebook"
    genericData = "genericData"
    string = "string"
    number = "number"
    integer = "integer"
    enum = "enum"
    array = "array"
    boolean = "boolean"


class Input(BaseModel):
    name: constr(regex=r"^[a-zA-Z0-9][-a-zA-Z0-9]*$") = Field(
        ...,
        description="Input name as expected by the plugin CLI",
        examples=["inputImages", "fileNamePattern", "thresholdValue"],
        title="Input name",
    )
    type: Type = Field(
        ..., examples=["collection", "string", "number"], title="Input Type"
    )
    description: constr(regex=r"^(.*)$") = Field(
        ..., examples=["Input Images"], title="Input description"
    )
    required: Optional[bool] = Field(
        True,
        description="Whether an input is required or not",
        examples=[True],
        title="Required input",
    )


class Type1(Enum):
    collection = "collection"
    stitchingVector = "stitchingVector"
    tensorflowModel = "tensorflowModel"
    tensorboardLogs = "tensorboardLogs"
    csvCollection = "csvCollection"
    pyramid = "pyramid"
    pyramidAnnotation = "pyramidAnnotation"
    genericData = "genericData"


class Output(BaseModel):
    name: constr(regex=r"^[a-zA-Z0-9][-a-zA-Z0-9]*$") = Field(
        ..., examples=["outputCollection"], title="Output name"
    )
    type: Type1 = Field(
        ..., examples=["stitchingVector", "collection"], title="Output type"
    )
    description: constr(regex=r"^(.*)$") = Field(
        ..., examples=["Output collection"], title="Output description"
    )


class UiItem(BaseModel):
    key: Union[Any, Any] = Field(
        ...,
        description="Key of the input which this UI definition applies to, the expected format is 'inputs.inputName'. Special keyword 'fieldsets' can be used to define arrangement of inputs by sections.",
        examples=["inputs.inputImages", "inputs.fileNamPattern", "fieldsets"],
        title="UI key",
    )


class CudaRequirements(BaseModel):
    deviceMemoryMin: Optional[float] = Field(
        0, examples=[100], title="Minimum device memory"
    )
    cudaComputeCapability: Optional[Union[str, List[Any]]] = Field(
        None,
        description="Specify either a single minimum value, or an array of valid values",
        examples=["8.0", ["3.5", "5.0", "6.0", "7.0", "7.5", "8.0"]],
        title="The cudaComputeCapability Schema",
    )


class ResourceRequirements(BaseModel):
    ramMin: Optional[float] = Field(
        None, examples=[2048], title="Minimum RAM in mebibytes (Mi)"
    )
    coresMin: Optional[float] = Field(
        None, examples=[1], title="Minimum number of CPU cores"
    )
    cpuAVX: Optional[bool] = Field(
        False,
        examples=[True],
        title="Advanced Vector Extensions (AVX) CPU capability required",
    )
    cpuAVX2: Optional[bool] = Field(
        False,
        examples=[False],
        title="Advanced Vector Extensions 2 (AVX2) CPU capability required",
    )
    gpu: Optional[bool] = Field(
        False, examples=[True], title="GPU/accelerator required"
    )
    cudaRequirements: Optional[CudaRequirements] = Field(
        {},
        examples=[{"deviceMemoryMin": 100, "cudaComputeCapability": "8.0"}],
        title="GPU Cuda-related requirements",
    )


class WippPluginManifest(BaseModel):
    name: constr(regex=r"^(.*)$", min_length=1) = Field(
        ...,
        description="Name of the plugin (format: org/name)",
        examples=["wipp/plugin-example"],
        title="Plugin name",
    )
    version: constr(regex=r"^(.*)$", min_length=1) = Field(
        ...,
        description="Version of the plugin (semantic versioning preferred)",
        examples=["1.0.0"],
        title="Plugin version",
    )
    title: constr(regex=r"^(.*)$", min_length=1) = Field(
        ...,
        description="Plugin title to display in WIPP forms",
        examples=["WIPP Plugin example"],
        title="Plugin title",
    )
    description: constr(regex=r"^(.*)$", min_length=1) = Field(
        ...,
        examples=["Custom image segmentation plugin"],
        title="Short description of the plugin",
    )
    author: Optional[Optional[constr(regex=r"^(.*)$")]] = Field(
        "", examples=["FirstName LastName"], title="Author(s)"
    )
    institution: Optional[Optional[constr(regex=r"^(.*)$")]] = Field(
        "",
        examples=["National Institute of Standards and Technology"],
        title="Institution",
    )
    repository: Optional[Optional[AnyUrl]] = Field(
        "",
        examples=["https://github.com/usnistgov/WIPP"],
        title="Source code repository",
    )
    website: Optional[Optional[AnyUrl]] = Field(
        "", examples=["http://usnistgov.github.io/WIPP"], title="Website"
    )
    citation: Optional[Optional[constr(regex=r"^(.*)$")]] = Field(
        "",
        examples=[
            "Peter Bajcsy, Joe Chalfoun, and Mylene Simon (2018). Web Microanalysis of Big Image Data. Springer-Verlag International"
        ],
        title="Citation",
    )
    containerId: constr(regex=r"^(.*)$") = Field(
        ...,
        description="Docker image ID",
        examples=["docker.io/wipp/plugin-example:1.0.0"],
        title="ContainerId",
    )
    baseCommand: Optional[List[str]] = Field(
        None,
        description="Base command to use while running container image",
        examples=[["python3", "/opt/executable/main.py"]],
        title="Base command",
    )
    inputs: List[Input] = Field(
        ...,
        description="Defines inputs to the plugin",
        title="List of Inputs",
        unique_items=True,
    )
    outputs: List[Output] = Field(
        ..., description="Defines the outputs of the plugin", title="List of Outputs"
    )
    ui: List[UiItem] = Field(..., title="Plugin form UI definition")
    resourceRequirements: Optional[ResourceRequirements] = Field(
        {},
        examples=[
            {
                "ramMin": 2048,
                "coresMin": 1,
                "cpuAVX": True,
                "cpuAVX2": False,
                "gpu": True,
                "cudaRequirements": {
                    "deviceMemoryMin": 100,
                    "cudaComputeCapability": "8.0",
                },
            }
        ],
        title="Plugin Resource Requirements",
    )
