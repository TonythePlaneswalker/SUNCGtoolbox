#!/bin/bash

for file in room/000*/*.obj
do (
	pcl_mesh_sampling $file ${file//obj/pcd} -no_vis_result #-write_normals
) done