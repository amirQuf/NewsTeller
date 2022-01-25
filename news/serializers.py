from .models import News ,Category  , Favcategory
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = ("name","slug",
			"is_active","position",)

  
class NewsSerializer(ModelSerializer):
	cat = CategorySerializer(many = True)
	class Meta:
		model = News
		fields = ('title','slug','desc','view','created',
			'publish','update','cat','thumbnail','status')

class FavcategorySerializer(ModelSerializer):
	Category = CategorySerializer()

	class Meta:
		model = Favcategory
		fields = ('user','Category',)

