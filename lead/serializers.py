from django.utils import timezone
from rest_framework import serializers
from .models import Lead, Company

class LeadSerializer(serializers.Serializer):
    PRODUCT_CHOICE = [
        ("BookKeeper", "BookKeeper"),
        ("Diparhta", "Dipartha"),
        ("MargBook", "MargBook")
    ]

    SOURCE_CHOICE = [
        ("Instagram", "Instagram"),
        ("FaceBook", "FaceBook"),
        ("Other", "Other")
    ]
    reference_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=150, required=True, help_text="Name field is required")
    organization_name = serializers.CharField(max_length=150, allow_blank=True)
    mobile_number = serializers.CharField(max_length=10, required=True, help_text="Enter mobile number of 10 digit only")
    phone_number = serializers.CharField(max_length=10, allow_blank=True)
    address = serializers.CharField(max_length=100, required=True, help_text="Address Field is required")
    product = serializers.ChoiceField(choices=PRODUCT_CHOICE, required=True, help_text="Product Field is required")
    email = serializers.EmailField(required=True, help_text="Email field is required")
    source = serializers.ChoiceField(choices=SOURCE_CHOICE, required=True, help_text='source field is required')

    def validate_email(self, value):
        if Lead.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
    
    def validate_mobile_number(self, value):
        if Lead.objects.filter(mobile_number=value).exists():
            raise serializers.ValidationError("Number already exists")
        return value
    
    def create(self, validated_data):
        request = self.context.get("request")

        lead = Lead.objects.create(
            name=validated_data['name'],
            organization_name=validated_data['organization_name'],
            mobile_number=validated_data['mobile_number'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            product=validated_data['product'],
            email=validated_data['email'],
            source=validated_data['source'],
            created_at=timezone.now(), 
            created_by=request.user
        )
        return lead
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.organization_name=validated_data.get('organization_name', instance.organization_name)
        instance.mobile_number=validated_data.get('mobile_number', instance.mobile_number)
        instance.phone_number=validated_data.get('phone_number', instance.phone_number)
        instance.address=validated_data.get('address', instance.address)
        instance.product=validated_data.get('product', instance.product)
        instance.email=validated_data.get('email', instance.email)
        instance.source=validated_data.get('source', instance.source)
        instance.updated_by=validated_data.get('updated_by', instance.updated_by)
        instance.updated_at=validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


class CompanySerializer(serializers.Serializer):
    reference_id = serializers.UUIDField(read_only=True)
    company_name = serializers.CharField(max_length=3, help_text="Company name is required")
    pan_number = serializers.CharField(max_length=9, required=True, help_text="Pan number is required")
    mobile_number = serializers.CharField(max_length=10, required=True, help_text="Mobile number is required")
    email = serializers.EmailField(required=True, help_text="Email is required")
    address = serializers.CharField(max_length=225, help_text="Address is required")
    contact_number = serializers.CharField(max_length=10, allow_blank=True, allow_null=True)

    def validate_email(self, value):
        if Company.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email Already exists")
        return value
    
    def validate_pan_number(self, value):
        if Company.objects.filter(pan_number=value).exists():
            raise serializers.ValidationError("Pan number is already registered")
        if len(value) != 9:
            raise serializers.ValidationError("Pan number must be 9 digits")
        if not value.isdigit():
            raise serializers.ValidationError("Pan number must be Digit")
        return value
    
    def validate_mobile_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must be digit")
        
        if not (value.startswith("97") or value.startswith("96") or value.startswith("98")):
            raise serializers.ValidationError("Mobile number must be start with 97, 98, or 96")
        
        if len(value) != 10:
            raise serializers.ValidationError("Mobile number must be 10 digits")
        
        return value
    
    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.pan_number = validated_data.get('pan_number', instance.pan_number)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.email = validated_data.get('email', instance.mobile)
        instance.address = validated_data.get('address', instance.address)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.updated_by=validated_data.get('updated_by', instance.updated_by)
        instance.updated_at=validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance







        





    
        