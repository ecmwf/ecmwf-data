# (C) Copyright 2021- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import os

import ecmwf.data as ecdata

PATH = os.path.dirname(__file__)


def test_data_read():
    fs = ecdata.read(os.path.join(PATH, "tuv_pl.grib"))
    assert len(fs) == 18
    sn = fs.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6


def test_data_fieldset_constructor():
    fs = ecdata.Fieldset(os.path.join(PATH, "tuv_pl.grib"))
    assert len(fs) == 18
    sn = fs.grib_get_string("shortName")
    assert sn == ["t", "u", "v"] * 6


def test_grib_index():
    grib_path = os.path.join(PATH, "tuv_pl.grib")
    fs = ecdata.read(grib_path)
    gi = fs.grib_index()
    assert isinstance(gi, list)
    assert len(gi) == 18
    for f, g in zip(fs, gi):
        assert g == (grib_path, f.grib_get_long("offset"))
    assert gi[5] == (grib_path, 7200)
