import os
from snakemake import shell

input_file = snakemake.input[0]
output_file = snakemake.output[0]

# 输出目录检查
output_dir = os.path.dirname(output_file)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)

# 支持列表或字符串
args = snakemake.params.get("gdalinfo_args", ["-stats"])
gdalinfo_args = " ".join(args) if isinstance(args, list) else args

# 构造命令
cmd = f"gdalinfo {gdalinfo_args} {input_file} > {output_file} 2>&1"
print("Running gdalinfo:", cmd)

# 将 stdout/stderr 写入 log文件
shell(cmd)
