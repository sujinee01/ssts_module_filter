# 엑셀 파일 읽기
from google.colab import drive
import pandas as pd

# Google Drive 마운트
drive.mount('/content/drive')

# 파일 경로 지정
file_path = "/content/drive/My Drive/example.xlsx"  # Google Drive에 저장된 엑셀 파일 경로

# 엑셀 파일 읽기
data = pd.read_excel(file_path, engine='openpyxl')

# 열 이름 정리 (공백 제거)
data.columns = data.columns.str.strip()

# 데이터 확인
print("데이터 프레임의 첫 5개 행:")
print(data.head())
print("\n데이터 프레임의 열 이름:")
print(data.columns)

# 사용자 입력받기: 사용할 모듈 입력
selected_modules = input("모듈을 선택하세요 (예: A,B,C): ").split(',')

# 선택한 모듈과 관련된 SSTS 필터링
result = []

for module in selected_modules:
    module = module.strip()  # 공백 제거
    if module in data.columns:
        # 해당 모듈과 관련된 SSTS 필터링
        module_ssts = data[data[module] == "x"]["module name"]
        for ssts in module_ssts:
            result.append({"SSTS": ssts, "Module": module})
    else:
        print(f"모듈 '{module}'은 데이터에 존재하지 않습니다.")

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(result).drop_duplicates()

# 결과 정렬 (SSTS와 Module을 기준으로 오름차순 정렬)
result_df = result_df.sort_values(by=["SSTS", "Module"]).reset_index(drop=True)

# 결과 출력
if not result_df.empty:
    print("\n선택된 모듈과 관련된 SSTS 목록 (오름차순 정렬):")
    print(result_df)
else:
    print("선택한 모듈과 관련된 SSTS가 없습니다.")
