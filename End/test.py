def calculate_clothing_coverage(gender, head, top, bottom, shoes):
    # 定义男性和女性的衣物覆盖率字典
    coverage_values = {
        'female': {
            'head': {'hat': 0.036},
            'top': {
                'long_sleeved': 0.404,
                'short_sleeved': 0.35,
                'vest': 0.266,
                'full_body_swimsuit': 0.4,
                'swimsuit': 0.134,
            },
            'bottom': {
                'trousers': 0.437,
                'long_shorts': 0.292,
                'long_skirt': 0.437,
                'middle_skirt': 0.292,
                'short_shorts': 0.213,
                'short_skirt': 0.213,
            },
            'shoes': {'shoes': 0.035, 'flip_flops': 0.00},
        },
        'male': {
            'head': {'hat': 0.036},
            'top': {
                'long_sleeved': 0.404,
                'short_sleeved': 0.35,
                'vest': 0.266,
            },
            'bottom': {
                'trousers': 0.437,
                'skateboard_shorts': 0.292,
                'shorts': 0.213,
                'swimming_trunks': 0.104,
            },
            'shoes': {'shoes': 0.035, 'flip_flops': 0.00},
        }
    }

    # 确保提供了有效的性别
    if gender not in coverage_values:
        print(f"Invalid gender: {gender}")
        return 0

    gender_coverage = coverage_values[gender]

    # 计算总覆盖率
    total_coverage = 0
    total_coverage += gender_coverage.get('head', {}).get(head, 0)
    print("This is the cloth", gender_coverage.get('head', {}))
    total_coverage += gender_coverage.get('top', {}).get(top, 0)
    print("This is the cloth", gender_coverage.get('top', {}))
    total_coverage += gender_coverage.get('bottom', {}).get(bottom, 0)
    print("This is the cloth", gender_coverage.get('bottom', {}))
    total_coverage += gender_coverage.get('shoes', {}).get(shoes, 0)
    print("This is the cloth", gender_coverage.get('shoes', {}))

    # 调试输出
    print(f"Total clothing coverage for {gender}: {total_coverage}")

    return total_coverage

def calculate_sunscreen_amount(gender, height, weight, head, top, bottom, shoes):
    # 先计算衣物的总覆盖率
    clothing_coverage = calculate_clothing_coverage(gender, head, top, bottom, shoes)
    
    # 根据身高、体重和衣物覆盖率计算防晒霜所需量
    bsa = 0.007184 * (height ** 0.725) * (weight ** 0.425) * 10000
    sunscreen_amount_ml = round((bsa * (1 - clothing_coverage)) * 0.002)
    sunscreen_teaspoons = round(sunscreen_amount_ml / 5, 2)  # 假设1茶匙=5ml

    # 调试输出
    print(f"BSA: {bsa}, Sunscreen amount (ml): {sunscreen_amount_ml}, Teaspoons: {sunscreen_teaspoons}")

    return {'teaspoons': sunscreen_teaspoons, 'milliliters': sunscreen_amount_ml}
