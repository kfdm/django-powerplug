from powerplug import ENTRY_POINT_NAV
from pkg_resources import working_set

def subnav(request):
    '''
    Loop through the entry points and build a sub navigation dictionary
    '''
    navigation = {}
    for entry in working_set.iter_entry_points(ENTRY_POINT_NAV):
        navigation.update(entry.load()(entry.name, request))
    return {'subnav': navigation}
