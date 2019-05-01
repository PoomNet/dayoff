from datetime import date

from django import forms


class Dayoffform(forms.Form):
    offtype = (
        ('ลากิจ', 'ลากิจ'),
        ('ลาป่วย', 'ลาป่วย'),
    )

    reason = forms.CharField(required=True,label="เนื่องจาก",widget=forms.Textarea)
    type=forms.ChoiceField(widget=forms.RadioSelect,choices=offtype,required=True,label="ประเภท")
    startdate = forms.DateField(required=True,label="ตั้งแต่วันที่")
    enddate = forms.DateField(required=True, label="ถึงวันที่")

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("startdate")
        end = cleaned_data.get("enddate")
        today = date.today()
        print(start.strftime('%Y-%m-%d') > end.strftime('%Y-%m-%d'))

        if start.strftime('%Y-%m-%d') < today.strftime('%Y-%m-%d'):
            raise forms.ValidationError("ห้ามเลือกวันในอดีต")
        elif end.strftime('%Y-%m-%d') < today.strftime('%Y-%m-%d'):
            raise forms.ValidationError("ห้ามเลือกวันในอดีต")
        elif start.strftime('%Y-%m-%d') > end.strftime('%Y-%m-%d'):
            raise forms.ValidationError("เลือกวันให้ถูกต้อง")