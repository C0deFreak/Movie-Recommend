from django.db import models

# All the details about a single project
class ProjectDetails(models.Model):

    # Unique project name to distinguish from other projects
    name = models.CharField(max_length=16, default='Project', unique=True)

    # Link to the github project page
    link = models.CharField(max_length=40, default='https://github.com/C0deFreak/Project', unique=True)

    # Is the project currently in development
    worked_on = models.BooleanField(default=False, unique=False)

