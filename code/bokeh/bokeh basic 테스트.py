from bokeh.plotting import figure, show

# from bokeh.plotting import output_file
# 출력파일 지정, 없으면 소스파일과 동일한 html 파일로 생성
# output_file("line.html")

p = figure()
# p = figure(plot_width=400, plot_height=400)

# add a line renderer
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5])
# p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

show(p)