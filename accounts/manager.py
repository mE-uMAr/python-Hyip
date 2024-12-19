from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self , p_number , password = None ,**extra_fields):
        if not p_number:
            raise ValueError("Phone number is required")
        extra_fields['email'] = self.normalize_email(extra_fields.get('email', ''))
        user = self.model(p_number = p_number , **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    
    def create_superuser(self , p_number , password = None , **extra_fields):
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        return self.create_user(p_number , password , **extra_fields)
