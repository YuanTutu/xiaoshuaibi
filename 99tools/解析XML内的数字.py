import matplotlib.pyplot as plt
import re

str = """<contour>
        <pt x="59" y="611" on="1"/>
        <pt x="42" y="698" on="1"/>
        <pt x="523" y="682" on="1"/>
        <pt x="523" y="627" on="1"/>
        <pt x="487" y="590" on="0"/>
        <pt x="419" y="491" on="0"/>
        <pt x="384" y="433" on="1"/>
        <pt x="342" y="382" on="0"/>
        <pt x="323" y="304" on="1"/>
        <pt x="297" y="241" on="0"/>
        <pt x="263" y="175" on="1"/>
        <pt x="262" y="83" on="0"/>
        <pt x="232" y="-26" on="1"/>
        <pt x="148" y="-26" on="1"/>
        <pt x="164" y="17" on="0"/>
        <pt x="160" y="63" on="1"/>
        <pt x="169" y="121" on="0"/>
        <pt x="185" y="192" on="1"/>
        <pt x="228" y="306" on="0"/>
        <pt x="271" y="405" on="1"/>
        <pt x="308" y="489" on="0"/>
        <pt x="341" y="538" on="1"/>
        <pt x="374" y="572" on="0"/>
        <pt x="403" y="611" on="1"/>
        <pt x="35" y="611" on="1"/>
      </contour>
"""


x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str)]
y = [int(i) for i in re.findall(r'y="(.*?)" on=', str)]

print(x)
print(y)

plt.plot(x, y)
plt.show()

"""
maoyan_dict = {
        'uniEC26': '1',
        'uniF081': '2',
        'uniE431': '8',
        'uniF724': '0',
        'uniF4B3': '3',
        'uniEBD9': '6',
        'uniE095': '5',
        'uniE506': '7',
        'uniF377': '9',
        'uniF824': '4',
}
"""