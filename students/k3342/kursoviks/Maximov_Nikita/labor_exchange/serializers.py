from rest_framework import serializers
from .models import Education, Profession, Field, Applicant, Resume, Course, CourseCertificate, Gratuity, Employer, Vacancy, Application


class EducationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Education
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    field = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Profession
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    professions = ProfessionSerializer(many=True)

    class Meta:
        model = Field
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Application
        fields = "__all__"


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Application
        fields = ('id', 'status')


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    employer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    education = serializers.SlugRelatedField(slug_field='name', read_only=True)
    profession = serializers.SlugRelatedField(slug_field='name', read_only=True)
    applications = ApplicationSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Vacancy
        fields = ('id', 'status', 'salary')


class ResumeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    applicant = serializers.SlugRelatedField(slug_field='fio', read_only=True)
    profession = serializers.SlugRelatedField(slug_field='name', read_only=True)
    applications = ApplicationSerializer(many=True)

    class Meta:
        model = Resume
        fields = "__all__"


class ResumeCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Resume
        fields = "__all__"


class ResumeUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Resume
        fields = ('id', 'rank', 'salary')


class CourseCertificateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Сертификат курса"""
    course = serializers.SlugRelatedField(slug_field='name', read_only=True)
    applicant = serializers.SlugRelatedField(slug_field='fio', read_only=True)

    class Meta:
        model = CourseCertificate
        fields = "__all__"


class CourseCertificateCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания записи в модели Сертификат курса"""

    class Meta:
        model = CourseCertificate
        fields = "__all__"


class GratuitySerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    applicant = serializers.SlugRelatedField(slug_field='fio', read_only=True)

    class Meta:
        model = Gratuity
        fields = "__all__"


class GratuityCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Gratuity
        fields = "__all__"


class GratuityUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Gratuity
        fields = ('id', 'date_end')


class ApplicantSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    education = serializers.SlugRelatedField(slug_field='name', read_only=True)
    resumes = ResumeSerializer(many=True)
    courses_certificates = CourseCertificateSerializer(many=True)
    gratuities = GratuitySerializer(many=True)

    class Meta:
        model = Applicant
        fields = "__all__"


class ApplicantCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Applicant
        fields = "__all__"


class ApplicantUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Applicant
        fields = ('id', 'address', 'age', 'work_experience', 'fio')


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    profession = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Course
        fields = "__all__"


class EmployerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = Employer
        fields = "__all__"


class ApplicationDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """
    resume = ResumeSerializer(many=False)
    vacancy = VacancySerializer(many=False)

    class Meta:
        model = Application
        fields = "__all__"
