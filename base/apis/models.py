from django.db import models

# Create your models here.

class UserModel(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fullName}'

class DetailsModel(models.Model):
    userId = models.TextField(max_length=100)
    surname = models.CharField(max_length=100)
    otherNames = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    profilePicture = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.userId} {self.surname} {self.otherNames}'

class FamEducationModel(models.Model):
    userId = models.TextField(max_length=200)
    fatherStatus = models.CharField(max_length=50)
    fatherSurname = models.CharField(max_length=100)
    fatherGivenName = models.CharField(max_length=100)
    fatherNationalId = models.CharField(max_length=50)
    fatherNationalIdPictureUrl = models.URLField()
    motherStatus = models.CharField(max_length=50)
    motherSurname = models.CharField(max_length=100)
    motherGivenName = models.CharField(max_length=100)
    motherNationalId = models.CharField(max_length=50)
    motherNationalIdPictureUrl = models.URLField()
    guardianSurname = models.CharField(max_length=100)
    guardianGivenName = models.CharField(max_length=100)
    guardianNationalId = models.CharField(max_length=50)
    guardianNationalIdPictureUrl = models.URLField()
    studentStatus = models.CharField(max_length=50)
    regNo = models.CharField(max_length=50)
    studentNo = models.CharField(max_length=50)
    courseName = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    artsOrSciences = models.CharField(max_length=50)
    yearOfStudy = models.CharField(max_length=10)
    currentCGPA = models.CharField(max_length=10)
    tuitionAmountPerSemester = models.CharField(max_length=20)
    pictureOfPortalUrl = models.URLField()
    schoolName = models.CharField(max_length=100)
    schoolLocation = models.CharField(max_length=100)
    yearOfSitting = models.CharField(max_length=10)
    subjectOneName = models.CharField(max_length=50)
    subjectOneGrade = models.CharField(max_length=10)
    subjectOnePoints = models.CharField(max_length=10)
    subjectTwoName = models.CharField(max_length=50)
    subjectTwoGrade = models.CharField(max_length=10)
    subjectTwoPoints = models.CharField(max_length=10)
    subjectThreeName = models.CharField(max_length=50)
    subjectThreeGrade = models.CharField(max_length=10)
    subjectThreePoints = models.CharField(max_length=10)
    subsidiaryOneName = models.CharField(max_length=50)
    subsidiaryOneGrade = models.CharField(max_length=10)
    subsidiaryOnePoints = models.CharField(max_length=10)
    subsidiaryTwoName = models.CharField(max_length=50)
    subsidiaryTwoGrade = models.CharField(max_length=10)
    subsidiaryTwoPoints = models.CharField(max_length=10)
    totalPoints = models.CharField(max_length=10)
    pictureOfPassSlipUrl = models.URLField()