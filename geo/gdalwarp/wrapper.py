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

cmd = f"gdalwarp {gdalwarp_args} {input_file} {output_file}"
print("Running gdalwarp:", cmd)

# 将 stdout/stderr 写入 log
shell(f"{cmd} > {snakemake.log[0]} 2>&1")
