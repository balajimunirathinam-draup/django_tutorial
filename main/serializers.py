from dataclasses import field
from rest_framework import serializers
from main.models import Note


class NoteSerializer(serializers.ModelSerializer):
    note_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = Note
        fields = [
            "note_id",
            "title",
            "description"
        ]