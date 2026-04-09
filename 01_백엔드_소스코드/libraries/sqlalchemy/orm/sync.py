# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sync.pyc (Python 3.11)

'''private module containing functions used for copying data
between instances based on join conditions.

'''
from __future__ import annotations
from  import exc
from  import util as orm_util
from base import PassiveFlag

def populate(source, source_mapper, dest, dest_mapper, synchronize_pairs, uowcommit, flag_cascaded_pks):
    source_dict = source.dict
    dest_dict = dest.dict
    for l, r in synchronize_pairs:
        prop = source_mapper._columntoproperty[l]
        value = source.manager[prop.key].impl.get(source, source_dict, PassiveFlag.PASSIVE_OFF)
    except exc.UnmappedColumnError:
        err = None
        _raise_col_to_prop(False, source_mapper, l, dest_mapper, r, err)
        err = None
        del err
    except:
        err = None
        del err
    prop = dest_mapper._columntoproperty[r]
    dest.manager[prop.key].impl.set(dest, dest_dict, value, None)


def bulk_populate_inherit_keys(source_dict, source_mapper, synchronize_pairs):
    for l, r in synchronize_pairs:
        prop = source_mapper._columntoproperty[l]
        value = source_dict[prop.key]
    except exc.UnmappedColumnError:
        err = None
        _raise_col_to_prop(False, source_mapper, l, source_mapper, r, err)
        err = None
        del err
    except:
        err = None
        del err
    prop = source_mapper._columntoproperty[r]
    source_dict[prop.key] = value
    continue
    except exc.UnmappedColumnError:
        err = None
        _raise_col_to_prop(True, source_mapper, l, source_mapper, r, err)
        err = None
        del err
        continue
        err = None
        del err


def clear(dest, dest_mapper, synchronize_pairs):
    for l, r in synchronize_pairs:
        if r.primary_key and dest_mapper._get_state_attr_by_column(dest, dest.dict, r) not in orm_util._none_set:
            raise AssertionError(f'''Dependency rule on column \'{l}\' tried to blank-out primary key column \'{r}\' on instance \'{orm_util.state_str(dest)}\'''')
        dest_mapper._set_state_attr_by_column(dest, dest.dict, r, None)
        except exc.UnmappedColumnError:
            err = None
            _raise_col_to_prop(True, None, l, dest_mapper, r, err)
            err = None
            del err
            continue
            err = None
            del err
        return None


def update(source, source_mapper, dest, old_prefix, synchronize_pairs):
    for l, r in synchronize_pairs:
        oldvalue = source_mapper._get_committed_attr_by_column(source.obj(), l)
        value = source_mapper._get_state_attr_by_column(source, source.dict, l, passive = PassiveFlag.PASSIVE_OFF)
    except exc.UnmappedColumnError:
        err = None
        _raise_col_to_prop(False, source_mapper, l, None, r, err)
        err = None
        del err
    except:
        err = None
        del err
    dest[r.key] = value
    dest[old_prefix + r.key] = oldvalue
    continue


def populate_dict(source, source_mapper, dict_, synchronize_pairs):
    for l, r in synchronize_pairs:
        value = source_mapper._get_state_attr_by_column(source, source.dict, l, passive = PassiveFlag.PASSIVE_OFF)
    except exc.UnmappedColumnError:
        err = None
        _raise_col_to_prop(False, source_mapper, l, None, r, err)
        err = None
        del err
    except:
        err = None
        del err
    dict_[r.key] = value
    continue


def source_modified(uowcommit, source, source_mapper, synchronize_pairs):
    '''return true if the source object has changes from an old to a
    new value on the given synchronize pairs

    '''
    for l, r in synchronize_pairs:
        prop = source_mapper._columntoproperty[l]
    except exc.UnmappedColumnError:
        err = None
        _raise_col_to_prop(False, source_mapper, l, None, r, err)
        err = None
        del err
    except:
        err = None
        del err
    history = uowcommit.get_attribute_history(source, prop.key, PassiveFlag.PASSIVE_NO_INITIALIZE)
    if bool(history.deleted):
        return True
    return False


def _raise_col_to_prop(isdest, source_mapper, source_column, dest_mapper, dest_column, err):
    if isdest:
        raise exc.UnmappedColumnError(f'''Can\'t execute sync rule for destination column \'{dest_column!s}\'; mapper \'{dest_mapper!s}\' does not map this column.  Try using an explicit `foreign_keys` collection which does not include this column (or use a viewonly=True relation).'''), err
    raise exc.UnmappedColumnError(f'''Can\'t execute sync rule for source column \'{source_column!s}\'; mapper \'{source_mapper!s}\' does not map this column.  Try using an explicit `foreign_keys` collection which does not include destination column \'{dest_column!s}\' (or use a viewonly=True relation).'''), err
