from ordering import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('realname', 'role', 'account', 'phone', 'password', 'latitude', 'longitude', 'balance', 'shopname')

class ShopSchema(ma.Schema):
    class Meta:
        fields = ('shopname', 'category', 'latitude', 'longitude')

class MealSchema(ma.Schema):
    class Meta:
        fields = ('name', 'shopname', 'image', 'price', 'quantity')

