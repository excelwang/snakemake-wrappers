import os
from snakemake import shell

input_file = snakemake.input[0]
output_file = snakemake.output[0]

# 输出目录存在性检查
output_dir = os.path.dirname(output_file)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)

# 支持列表或字符串
args = snakemake.params.get("gdalwarp_args", ["-overwrite", "-t_srs", "EPSG:4326", "-r", "bilinear"])
gdalwarp_args = " ".join(args) if isinstance(args, list) else args

# # 容器镜像
# container_image = "docker://docker.1ms.run/osgeo/gdal:ubuntu-small-3.6.3"

# # 构造命令：容器执行
# cmd = f"apptainer exec {container_image} gdalwarp {gdalwarp_args} {input_file} {output_file}"
# print("Running gdalwarp in container:", cmd)

# # 执行命令
# shell(cmd)

cmd = f"gdalwarp {gdalwarp_args} {input_file} {output_file}"
print("Running gdalwarp:", cmd)

# 将 stdout/stderr 写入 log
shell(f"{cmd} > {snakemake.log[0]} 2>&1")
