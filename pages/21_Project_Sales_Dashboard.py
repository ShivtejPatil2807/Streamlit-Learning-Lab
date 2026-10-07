import numpy as np
import pandas as pd
import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section, show_setup

lesson_page(
    21,
    "Explore two years of sales data with filters, key numbers and graphs, "
    "using nothing but pandas and Streamlit.",
)


@show_setup
def make_sales():
    rng = np.random.default_rng(42)  # a fixed seed, so everyone gets the same data
    prices = {"Laptop": 900, "Phone": 600, "Tablet": 400}
    rows = []
    for number, month in enumerate(pd.date_range("2024-01-01", periods=24, freq="MS")):
        for region in ["North", "South", "East", "West"]:
            for product, price in prices.items():
                orders = int(rng.integers(20, 80) * (1 + 0.02 * number))
                rows.append(
                    {
                        "Month": month,
                        "Region": region,
                        "Product": product,
                        "Orders": orders,
                        "Revenue": orders * price,
                    }
                )
    return pd.DataFrame(rows)


sales = make_sales()

section(
    "The idea",
    "A dashboard turns a table of numbers into something you can explore. Here the table is "
    "made-up sales: 24 months, 4 regions and 3 products. You will look at it, summarise it with "
    "pandas, filter it with widgets, and then put everything together.",
)


@demo(
    "Look at the data",
    "A pandas DataFrame is a table. head() shows the first rows, and len() counts them.",
)
def _():
    st.dataframe(sales.head(8))
    st.write(f"{len(sales)} rows and {len(sales.columns)} columns")


@demo(
    "Summarise with groupby",
    "groupby() splits the table into groups, and sum() adds each group up. "
    "Streamlit can draw the result straight away.",
)
def _():
    revenue_by_month = sales.groupby("Month")["Revenue"].sum()
    revenue_by_region = sales.groupby("Region")["Revenue"].sum()

    st.write("Revenue by month")
    st.line_chart(revenue_by_month)
    st.write("Revenue by region")
    st.bar_chart(revenue_by_region)


@demo(
    "Filter with widgets",
    "Widgets give you values. isin() keeps the rows whose value is in a list.",
)
def _():
    regions = st.multiselect("Regions", sorted(sales["Region"].unique()), default=["North", "South"])
    product = st.selectbox("Product", ["All"] + sorted(sales["Product"].unique()))

    view = sales[sales["Region"].isin(regions)]
    if product != "All":
        view = view[view["Product"] == product]

    st.write(f"{len(view)} of {len(sales)} rows")
    st.dataframe(view.head(10))


@demo(
    "The dashboard",
    "Filters, key numbers and graphs together. Change the filters and everything updates.",
    caption="Pick at least one region and one product to see the numbers.",
)
def _():
    regions = sorted(sales["Region"].unique())
    products = sorted(sales["Product"].unique())

    left, right = st.columns(2)
    show_regions = left.multiselect("Show regions", regions, default=regions)
    show_products = right.multiselect("Show products", products, default=products)

    view = sales[sales["Region"].isin(show_regions) & sales["Product"].isin(show_products)]

    if view.empty:
        st.warning("Pick at least one region and one product.")
    else:
        revenue = int(view["Revenue"].sum())
        orders = int(view["Orders"].sum())

        first, second, third = st.columns(3)
        first.metric("Revenue", f"${revenue:,}")
        second.metric("Orders", f"{orders:,}")
        third.metric("Average order", f"${revenue / orders:,.0f}")

        st.line_chart(view.groupby("Month")["Revenue"].sum())
        st.bar_chart(view.groupby("Product")["Revenue"].sum())


lesson_footer(21)
