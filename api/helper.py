from rest_framework import filters

class CustomSearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        print(self.request.user.user_role,'==========================')
        if self.request.user.user_role == "C":
            print('C')
            return ['Username','Name','city']
        elif self.request.user.user_role == "A":
            print('a')
            return ['name','desc']
        # return ['name','desc']
        # return super().get_search_fields(view, request)