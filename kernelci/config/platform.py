# SPDX-License-Identifier: LGPL-2.1-or-later
#
# Copyright (C) 2024 Collabora Limited
# Author: Arnaud Ferraris <arnaud.ferraris@collabora.com>

"""KernelCI platform configuration"""

from .base import YAMLConfigObject


# pylint: disable=too-many-instance-attributes
class Platform(YAMLConfigObject):
    """Platform configuration definition"""

    yaml_tag = '!Platform'

    # pylint: disable=too-many-arguments
    def __init__(self, name, arch="x86_64", base_name=None,
                 boot_method="grub", context=None, dtb=None, mach="x86",
                 params=None):
        self._name = name
        self._arch = arch
        self._base_name = base_name
        self._boot_method = boot_method
        self._context = context
        self._dtb = dtb
        self._mach = mach
        self._params = params

    @property
    def name(self):
        """Platform name"""
        return self._name

    @property
    def arch(self):
        """Platform architecture"""
        return self._arch

    @property
    def base_name(self):
        """Platform base name"""
        return self._base_name if self._base_name else self._name

    @property
    def boot_method(self):
        """Platform boot method"""
        return self._boot_method

    @property
    def context(self):
        """Context variables used for platform boot"""
        return dict(self._context) if self._context else None

    @property
    def dtb(self):
        """Platform dtb file name"""
        return self._dtb

    @property
    def mach(self):
        """Platform sub-architecture"""
        return self._mach

    @property
    def params(self):
        """Arbitrary parameters passed to the template"""
        return dict(self._params) if self._params else None

    @classmethod
    def _get_yaml_attributes(cls):
        attrs = super()._get_yaml_attributes()
        attrs.update({
            'arch',
            'base_name',
            'boot_method',
            'context',
            'dtb',
            'mach',
            'params',
        })
        return attrs


def from_yaml(data, _):
    """Create the platforms configurations using data loaded from YAML"""
    platforms = {
        name: Platform.load_from_yaml(config, name=name)
        for name, config in data.get('platforms', {}).items()
    }

    return {
        'platforms': platforms,
    }
