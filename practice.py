import pandas as pd

# 엑셀 파일 읽기
file_path = "your_excel_file.xlsx"  # 엑셀 파일 경로
data = pd.read_excel(file_path)

# 사용자 입력받기: 사용할 모듈 입력
selected_modules = input("모듈을 선택하세요 (예: A,B,C): ").split(',')

# 선택한 모듈과 관련된 SSTS 필터링
result = []

for module in selected_modules:
    module = module.strip()  # 공백 제거
    if module in data.columns:
        # 해당 모듈과 관련된 SSTS 필터링
        module_ssts = data[data[module] == "x"]["SSTS name"]
        for ssts in module_ssts:
            result.append({"SSTS": ssts, "Module": module})

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(result).drop_duplicates()

# 결과 출력
if not result_df.empty:
    print("\n선택된 모듈과 관련된 SSTS 목록:")
    print(result_df)
else:
    print("선택한 모듈과 관련된 SSTS가 없습니다.")
