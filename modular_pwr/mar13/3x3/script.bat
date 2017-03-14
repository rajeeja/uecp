#!/bin/bash
rm cubit* history*
# running assygen
rm in3.sat in3.py in3.jou in3.template.jou
/Users/rajeevjain/mk/buildmkface/tools/assygen in3
cubit -nographics in3.py
rm geom_3x3.sat
cubit -nographics geom_in3.py
cubit -nographics mesh_in3.jou
