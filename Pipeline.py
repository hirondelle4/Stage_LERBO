###############SNAKEMAKE################################

## conda install -c conda-forge mamba
## mamba create -c conda-forge -c bioconda -n snakemake snakemake

########################################################
rule all:
    input:
        "./qualityC/pycoQC_output_min_pass_q10.html"

rule qualityC:
    input:
        "./sequencing_summary.txt"
    output:
        "./qualityC/pycoQC_output_min_pass_q10.html"
    threads: 8
    conda:
        "envs/pycoqc.yaml"
    shell:
        "pycoQC  --summary_file {input} --html_outfile {output} --min_pass_qual 10"
