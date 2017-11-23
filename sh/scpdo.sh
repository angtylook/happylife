#!/bin/sh

echo =======begin====================

for rel in rel1 rel2 rel3 rel4 rel5 rel6 rel7 rel8
do
    echo =======copy to $rel=====================
    scp ${1} $rel:${2}
done

echo =======end======================

