'''
Created on Mar 19, 2015

@author: ayan
'''


def find_grid_topology_vars(nc):
    """
    Get the variables from a netCDF dataset
    that have a cf_role attribute of 'grid_topology'.
    
    :params nc: netCDF dataset
    :type nc: netCDF4.Dataset
    :return: list of variables that contain grid topologies
    :rtype: list
    
    """
    nc_vars = nc.variables
    grid_topology_vars = []
    for nc_var in nc_vars.iterkeys():
        nc_var_obj = nc.variables[nc_var]
        try:
            cf_role = nc_var_obj.cf_role.strip()
            topology_dim = nc_var_obj.topology_dimension
        except AttributeError:
            cf_role = None
            topology_dim = None
        if cf_role == 'grid_topology' and topology_dim == 2:
            grid_topology_vars.append(nc_var)
    return grid_topology_vars


def sgrid_compliant_file(nc):
    """
    Determine whether a dataset is
    SGRID compliant.
    
    :param nc: netCDF dataset
    :type nc: netCDF4.Dataset
    :return: True if dataset is compliant, False if it is not
    :rtype: bool
    
    """
    grid_vars = find_grid_topology_vars(nc)
    if len(grid_vars) > 0:
        sgrid_compliant = True
    else:
        sgrid_compliant = False
    return sgrid_compliant