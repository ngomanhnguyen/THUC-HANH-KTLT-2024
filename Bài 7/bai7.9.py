print("Ngo MAnh Nguyen MSSV: 235752021610058")
def copy_file(source_file, destination_file):
    """Sao chép nội dung từ một tệp sang tệp khác.

    Args:
        source_file (str): Đường dẫn đến tệp nguồn.
        destination_file (str): Đường dẫn đến tệp đích.
    """

    with open(source_file, 'r') as f_in:
        with open(destination_file, 'w') as f_out:
            for line in f_in:
                f_out.write(line)

# Ví dụ sử dụng:
copy_file('nhap tep 1', 'nhap tep 2')
