class StyleDesign:
    """款式设计"""

    def __init__(
        self,
        third_level_category,
        launch_year,
        launch_season,
        applicable_gender,
        fourth_level_category,
        design_style,
        design_draft,
    ):
        self.third_level_category = third_level_category  # 三级分类
        self.launch_year = launch_year  # 上市年份
        self.launch_season = launch_season  # 上市季节
        self.applicable_gender = applicable_gender  # 适用性别
        self.fourth_level_category = fourth_level_category  # 四级分类
        self.design_style = design_style  # 设计风格
        self.design_draft = design_draft  # 设计稿
