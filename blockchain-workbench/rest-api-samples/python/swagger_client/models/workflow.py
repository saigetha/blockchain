# coding: utf-8

"""
    Azure Blockchain Workbench REST API

    The Azure Blockchain Workbench REST API is a Workbench extensibility point, which allows developers to create and manage blockchain applications, manage users and organizations within a consortium, integrate blockchain applications into services and platforms, perform transactions on a blockchain, and retrieve transactional and contract data from a blockchain.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.workflow_function import WorkflowFunction  # noqa: F401,E501
from swagger_client.models.workflow_property import WorkflowProperty  # noqa: F401,E501
from swagger_client.models.workflow_state import WorkflowState  # noqa: F401,E501


class Workflow(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'display_name': 'str',
        'application_id': 'int',
        'constructor_id': 'int',
        'start_state_id': 'int',
        'initiators': 'list[str]',
        'properties': 'list[WorkflowProperty]',
        'constructor': 'WorkflowFunction',
        'functions': 'list[WorkflowFunction]',
        'start_state': 'WorkflowState',
        'states': 'list[WorkflowState]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'display_name': 'displayName',
        'application_id': 'applicationId',
        'constructor_id': 'constructorId',
        'start_state_id': 'startStateId',
        'initiators': 'initiators',
        'properties': 'properties',
        'constructor': 'constructor',
        'functions': 'functions',
        'start_state': 'startState',
        'states': 'states'
    }

    def __init__(self, id=None, name=None, description=None, display_name=None, application_id=None, constructor_id=None, start_state_id=None, initiators=None, properties=None, constructor=None, functions=None, start_state=None, states=None):  # noqa: E501
        """Workflow - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._display_name = None
        self._application_id = None
        self._constructor_id = None
        self._start_state_id = None
        self._initiators = None
        self._properties = None
        self._constructor = None
        self._functions = None
        self._start_state = None
        self._states = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if application_id is not None:
            self.application_id = application_id
        if constructor_id is not None:
            self.constructor_id = constructor_id
        if start_state_id is not None:
            self.start_state_id = start_state_id
        if initiators is not None:
            self.initiators = initiators
        if properties is not None:
            self.properties = properties
        if constructor is not None:
            self.constructor = constructor
        if functions is not None:
            self.functions = functions
        if start_state is not None:
            self.start_state = start_state
        if states is not None:
            self.states = states

    @property
    def id(self):
        """Gets the id of this Workflow.  # noqa: E501


        :return: The id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workflow.


        :param id: The id of this Workflow.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Workflow.  # noqa: E501


        :return: The name of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workflow.


        :param name: The name of this Workflow.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Workflow.  # noqa: E501


        :return: The description of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workflow.


        :param description: The description of this Workflow.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this Workflow.  # noqa: E501


        :return: The display_name of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Workflow.


        :param display_name: The display_name of this Workflow.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def application_id(self):
        """Gets the application_id of this Workflow.  # noqa: E501


        :return: The application_id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this Workflow.


        :param application_id: The application_id of this Workflow.  # noqa: E501
        :type: int
        """

        self._application_id = application_id

    @property
    def constructor_id(self):
        """Gets the constructor_id of this Workflow.  # noqa: E501


        :return: The constructor_id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._constructor_id

    @constructor_id.setter
    def constructor_id(self, constructor_id):
        """Sets the constructor_id of this Workflow.


        :param constructor_id: The constructor_id of this Workflow.  # noqa: E501
        :type: int
        """

        self._constructor_id = constructor_id

    @property
    def start_state_id(self):
        """Gets the start_state_id of this Workflow.  # noqa: E501


        :return: The start_state_id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._start_state_id

    @start_state_id.setter
    def start_state_id(self, start_state_id):
        """Sets the start_state_id of this Workflow.


        :param start_state_id: The start_state_id of this Workflow.  # noqa: E501
        :type: int
        """

        self._start_state_id = start_state_id

    @property
    def initiators(self):
        """Gets the initiators of this Workflow.  # noqa: E501


        :return: The initiators of this Workflow.  # noqa: E501
        :rtype: list[str]
        """
        return self._initiators

    @initiators.setter
    def initiators(self, initiators):
        """Sets the initiators of this Workflow.


        :param initiators: The initiators of this Workflow.  # noqa: E501
        :type: list[str]
        """

        self._initiators = initiators

    @property
    def properties(self):
        """Gets the properties of this Workflow.  # noqa: E501


        :return: The properties of this Workflow.  # noqa: E501
        :rtype: list[WorkflowProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Workflow.


        :param properties: The properties of this Workflow.  # noqa: E501
        :type: list[WorkflowProperty]
        """

        self._properties = properties

    @property
    def constructor(self):
        """Gets the constructor of this Workflow.  # noqa: E501


        :return: The constructor of this Workflow.  # noqa: E501
        :rtype: WorkflowFunction
        """
        return self._constructor

    @constructor.setter
    def constructor(self, constructor):
        """Sets the constructor of this Workflow.


        :param constructor: The constructor of this Workflow.  # noqa: E501
        :type: WorkflowFunction
        """

        self._constructor = constructor

    @property
    def functions(self):
        """Gets the functions of this Workflow.  # noqa: E501


        :return: The functions of this Workflow.  # noqa: E501
        :rtype: list[WorkflowFunction]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this Workflow.


        :param functions: The functions of this Workflow.  # noqa: E501
        :type: list[WorkflowFunction]
        """

        self._functions = functions

    @property
    def start_state(self):
        """Gets the start_state of this Workflow.  # noqa: E501


        :return: The start_state of this Workflow.  # noqa: E501
        :rtype: WorkflowState
        """
        return self._start_state

    @start_state.setter
    def start_state(self, start_state):
        """Sets the start_state of this Workflow.


        :param start_state: The start_state of this Workflow.  # noqa: E501
        :type: WorkflowState
        """

        self._start_state = start_state

    @property
    def states(self):
        """Gets the states of this Workflow.  # noqa: E501


        :return: The states of this Workflow.  # noqa: E501
        :rtype: list[WorkflowState]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this Workflow.


        :param states: The states of this Workflow.  # noqa: E501
        :type: list[WorkflowState]
        """

        self._states = states

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other