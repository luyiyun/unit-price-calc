import flet as ft


class UnitPriceCalculator(ft.Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()
        self.new_quantity = ft.TextField(label="数量", expand=True)
        self.new_price = ft.TextField(label="价格", expand=True)
        self.unit_prices = []
        self.unit_price_list = ft.Column()

        self.width = 600
        self.controls = [
            ft.Row(
                [
                    ft.Text(
                        value="Unit Price Calculator",
                        theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    self.new_quantity,
                    self.new_price,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.unit_price_list,
        ]

    def add_clicked(self, e):
        if self.new_quantity.value and self.new_price.value:
            if (
                not self.new_quantity.value.isdigit()
                or not self.new_price.value.isdigit()
            ):
                return

            up = float(self.new_price.value) / float(self.new_quantity.value)
            self.unit_prices.append(up)
            min_unit_price = min(self.unit_prices)

            for control, upi in zip(
                self.unit_price_list.controls, self.unit_prices[:-1]
            ):
                control.controls[0].bgcolor = (
                    "red" if upi == min_unit_price else None
                )

            self.unit_price_list.controls.append(
                ft.Row(
                    [
                        ft.Text(
                            f"序号: {len(self.unit_prices)}, 单价：{up:.5f}",
                            bgcolor="red" if up == min_unit_price else None,
                            text_align=ft.TextAlign.CENTER,
                            size=25,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

            self.update()


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # create app control and add it to the page
    page.add(ft.SafeArea(UnitPriceCalculator(), expand=True))

    page.adaptive = True


ft.app(main)
