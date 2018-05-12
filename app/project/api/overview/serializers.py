from rest_framework import serializers

from project.api.project_apps.project_assignment.serializers import ProjectAssignmentSerializer
from project.api.project_apps.project_data.serializers import ProjectDataSerializer


class OverviewSerializer(serializers.Serializer):
    project_data = ProjectDataSerializer(many=True)
    project_roles = ProjectAssignmentSerializer(many=True)