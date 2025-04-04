### Reference: https://blog.csdn.net/qq_35629563/article/details/133499112
import pypdf

# 設定檔案路徑
file_name = "C:\\Lecture\\InformationTheory\\Ch1.pdf"
output_file_name = "C:\\Lecture\\InformationTheory\\InformationTheoryLearningNotes.pdf"

# 打開 PDF 並讀取內容
reader = pypdf.PdfReader(file_name)
writer = pypdf.PdfWriter()

# 將所有頁面從 reader 複製到 writer
for page_num in range(len(reader.pages)):
    writer.add_page(reader.pages[page_num])

'''
# 顯示原始大綱（如果存在）
def display_outlines(outlines, level=0):
    for item in outlines:
        if isinstance(item, list):  # 如果是子大綱，遞歸處理
            display_outlines(item, level + 1)
        else:
            print("  " * level + f"{item.title} (Page {item.page + 1})")  # 頁碼從 1 開始顯示

# 顯示大綱
outlines = reader._get_outline()
print("原始大綱:")
display_outlines(outlines)
'''


# 添加新的大綱（書籤）
# 假設你想在第 1 頁（0 索引）添加書籤
chap1 = writer.add_outline_item(title='1. Introduction', page_number=0, parent=None)  # 頁碼是從 0 開始的

chap2 = writer.add_outline_item(title='2. Entropy, Relative Entropy and Mutual Information', page_number=2, parent=None)
chap2_1 = writer.add_outline_item(title='2.1 Entropy', page_number=2, parent=chap2)
chap2_2 = writer.add_outline_item(title='2.2 Convex Function and Jenson\'s Inequality', page_number=3, parent=chap2)
chap2_3 = writer.add_outline_item(title='2.3 Joint Entropy and Conditional Entropy', page_number=4, parent=chap2)
chap2_4 = writer.add_outline_item(title='2.4 Relative Entropy and Mutual Information', page_number=5, parent=chap2)
chap2_5 = writer.add_outline_item(title='2.5 Chain Rules for Entropy, Relative Entropy and Mutual Information', page_number=7, parent=chap2)
chap2_6 = writer.add_outline_item(title='2.6 Log Sum Inequality and Its Applications', page_number=9, parent=chap2)
chap2_7 = writer.add_outline_item(title='2.7 Data Processing Inequality', page_number=11, parent=chap2)
chap2_8 = writer.add_outline_item(title='2.8 Fano\'s Inequality', page_number=12, parent=chap2)

chap3 = writer.add_outline_item(title='3. Asymptotic Equipartition Property', page_number=14, parent=None)
chap3_1 = writer.add_outline_item(title='3.1 Convergence of Random Variables', page_number=14, parent=chap3)
chap3_2 = writer.add_outline_item(title='3.2 Markov\'s and Chebyshev\'s Inqualities and Weak Law of Large Numbers', page_number=14, parent=chap3)
chap3_3 = writer.add_outline_item(title='3.3 Asymptotic Equipartition Property (AEP)', page_number=15, parent=chap3)
chap3_4 = writer.add_outline_item(title='3.4 Typical Set', page_number=16, parent=chap3)
chap3_4 = writer.add_outline_item(title='3.5 High-Probability Sets', page_number=19, parent=chap3)

chap4 = writer.add_outline_item(title='4. Entropy Rates of a Stochastic Process', page_number=21, parent=None)
chap4_1 = writer.add_outline_item(title='4.1 Markov Chains', page_number=21, parent=chap4)
chap4_2 = writer.add_outline_item(title='4.2 Entropy Rate', page_number=24, parent=chap4)

chap5 = writer.add_outline_item(title='5. Data Compression', page_number=28, parent=None)
chap5_1 = writer.add_outline_item(title='5.1 Example of Source Codes', page_number=28, parent=chap5)
chap5_2 = writer.add_outline_item(title='5.2 Kraft-McMillan Theorem', page_number=29, parent=chap5)

# 將修改後的 PDF 寫入新的文件
with open(output_file_name, "wb") as output:
    writer.write(output)

print(f"成功寫入新文件: {output_file_name}")






### 添加子書籤
"""
parent_bookmark_0 = writer.add_outline_item(title='test', page_number=1, parent=None)
writer.add_outline_item(title='test', page_number=2, parent=parent_bookmark_0)
"""

### 顯示內容
"""
# 打開 PDF 檔案
input_file = "path_to_pdf.pdf"
reader = pypdf.PdfReader(input_file)

# 提取並顯示每一頁的文字
for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    text = page.extract_text()
    print(f"Page {page_num + 1} content:\n{text}\n")
"""


