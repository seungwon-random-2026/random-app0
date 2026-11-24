# 1. 함수(def): 음식 재료 속에 알레르기 성분이 있는지 검사하는 함수
def check_allergy(my_allergies, food_ingredients):
    detected = []  # 발견된 알레르기 성분을 담을 리스트
    
    # 2. 반복구조(for): 음식 재료를 하나씩 확인
    for ingredient in food_ingredients:
        if ingredient in my_allergies:
            detected.append(ingredient)
            
    return detected

# 도표 출력 및 안전/위험 음식 분류 함수(def)
def print_summary_table(records, safe_foods, danger_foods):
    print("\n" + "=" * 70)
    print(f"{'음식 이름':<14} | {'섭취 여부':<10} | {'포함된 알레르기 유발 성분'}")
    print("-" * 70)
    
    # 반복구조(for): 기록된 음식 데이터를 도표로 출력
    for row in records:
        food = row[0]
        status = row[1]
        allergens = row[2]
        print(f"{food:<14} | {status:<10} | {allergens}")
        
    print("=" * 70)
    
    # 최종 식단 가이드 출력
    print("\n[최종 식단 가이드]")
    print("▶ 먹어도 되는 음식 (안전):", ", ".join(safe_foods) if safe_foods else "없음")
    print("▶ 먹으면 안 되는 음식 (위험):", ", ".join(danger_foods) if danger_foods else "없음")
    print("=" * 70)

# 메인 프로그램 실행 함수
def main():
    print("=== 알레르기 유발 식품 판별기 ===")
    
    # 3. 리스트(list): 미리 등록된 기본 음식 데이터 [음식명, [재료 리스트]]
    default_foods = [
        ["까르보나라", ["밀가루", "우유", "계란", "베이컨", "치즈"]],
        ["새우볶음밥", ["쌀", "새우", "계란", "당근", "대파"]],
        ["양념치킨", ["닭고기", "밀가루", "땅콩", "간장", "마늘"]],
        ["된장찌개", ["대두", "두부", "애호박", "양파", "멸치"]],
        ["페퍼로니피자", ["밀가루", "치즈", "우유", "돼지고기", "토마토"]],
        ["복숭아아이스티", ["복숭아", "설탕", "홍차"]],
        ["고등어구이", ["고등어", "소금"]],
        ["소고기미역국", ["소고기", "미역", "참기름", "마늘", "간장"]],
        ["삼겹살구이", ["돼지고기", "상추", "마늘", "쌈장"]],
        ["과일샐러드", ["사과", "바나나", "양상추", "방울토마토"]],
        ["현미밥", ["현미", "쌀", "물"]]
    ]

    # 사용자 알레르기 입력받기
    user_input = input("본인의 알레르기 성분을 쉼표(,)로 구분해 입력하세요 (예: 우유, 땅콩, 새우): ")
    my_allergies = [item.strip() for item in user_input.split(",") if item.strip()]
    
    if not my_allergies:
        print("등록된 알레르기가 없습니다. 모든 음식을 드실 수 있습니다!")
        return

    print(f"\n-> 등록된 알레르기: {my_allergies}")
    print("-> 기본 등록된 11가지 음식을 먼저 검사합니다...\n")

    records = []       # 도표 출력용 리스트
    safe_foods = []    # 먹어도 되는 음식 리스트
    danger_foods = []  # 먹으면 안 되는 음식 리스트

    # 4-1. 반복구조(for): 미리 등록된 음식들을 먼저 자동 검사
    for food_item in default_foods:
        f_name = food_item[0]
        f_ings = food_item[1]
        
        danger_list = check_allergy(my_allergies, f_ings)
        
        # 선택구조(if - else)로 안전/위험 분류
        if len(danger_list) > 0:
            allergen_str = ", ".join(danger_list)
            danger_foods.append(f_name)
            records.append([f_name, "섭취 불가", allergen_str])
        else:
            safe_foods.append(f_name)
            records.append([f_name, "섭취 가능", "없음"])

    print("기본 음식 검사가 완료되었습니다! 추가로 검사할 음식이 있다면 입력하세요.")

    # 4-2. 반복구조(while): 사용자가 원하는 음식을 추가로 계속 입력
    while True:
        food_name = input("\n추가로 검사할 음식 이름 (결과 보기 및 종료는 '종료' 입력): ").strip()
        
        # 5. 선택구조(if - elif - else)
        if food_name == "종료":
            print("\n모든 검사를 마치고 최종 도표를 출력합니다...")
            break
            
        elif food_name == "":
            print("음식 이름을 정확히 입력해주세요.")
            continue
            
        else:
            ing_input = input(f"'{food_name}'에 들어간 재료를 쉼표(,)로 구분해 입력하세요: ")
            food_ingredients = [item.strip() for item in ing_input.split(",") if item.strip()]
            
            danger_list = check_allergy(my_allergies, food_ingredients)
            
            if len(danger_list) > 0:
                allergen_str = ", ".join(danger_list)
                print(f"[위험!] '{food_name}'에는 알레르기 성분({allergen_str})이 들어있습니다.")
                danger_foods.append(food_name)
                records.append([food_name, "섭취 불가", allergen_str])
            else:
                print(f"[안전] '{food_name}'에는 알레르기 성분이 없습니다.")
                safe_foods.append(food_name)
                records.append([food_name, "섭취 가능", "없음"])

    # 최종 도표 및 먹어도 되는/안 되는 음식 목록 출력
    print_summary_table(records, safe_foods, danger_foods)

# 프로그램 시작
if __name__ == "__main__":
    main()
