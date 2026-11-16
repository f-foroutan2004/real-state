from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PropertyForm
from .models import Property

from django.shortcuts import get_object_or_404


@login_required
def property_create_view(request):

    if request.user.role != 'agent':
        messages.error(request, 'فقط مشاور املاک می‌تواند ملک ثبت کند.')
        return redirect('home')

    if request.method == 'POST':
        form = PropertyForm(request.POST)

        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            form.save_m2m()

            messages.success(request, 'ملک با موفقیت ثبت شد.')
            return redirect('home')

    else:
        form = PropertyForm()

    return render(
        request,
        'properties/property_form.html',
        {'form': form}
    )


def property_list_view(request):
    properties = Property.objects.all().order_by('-id')

    city = request.GET.get('city')
    status = request.GET.get('status')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_area = request.GET.get('min_area')
    max_area = request.GET.get('max_area')
    rooms = request.GET.get('rooms')

    if city:
        properties = properties.filter(city__icontains=city)

    if status:
        properties = properties.filter(status=status)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    if min_area:
        properties = properties.filter(area__gte=min_area)

    if max_area:
        properties = properties.filter(area__lte=max_area)

    if rooms:
        properties = properties.filter(rooms=rooms)

    return render(
        request,
        'properties/property_list.html',
        {'properties': properties}
    )


def property_detail_view(request, pk):
    property = get_object_or_404(Property, pk=pk)

    return render(
        request,
        'properties/property_detail.html',
        {'property': property}
    )

@login_required
def property_edit_view(request, pk):

    if request.user.role != 'agent':
        messages.error(request, 'فقط مشاور املاک اجازه ویرایش ملک را دارد.')
        return redirect('home')

    property = get_object_or_404(
        Property,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)

        if form.is_valid():
            form.save()
            messages.success(request, 'ملک با موفقیت ویرایش شد.')
            return redirect('property_list')

    else:
        form = PropertyForm(instance=property)

    return render(
        request,
        'properties/property_form.html',
        {'form': form}
    )

@login_required
def property_delete_view(request, pk):

    if request.user.role != 'agent':
        messages.error(request, 'فقط مشاور املاک اجازه حذف ملک را دارد.')
        return redirect('home')

    property = get_object_or_404(
        Property,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        property.delete()
        messages.success(request, 'ملک با موفقیت حذف شد.')
        return redirect('property_list')

    return render(
        request,
        'properties/property_confirm_delete.html',
        {'property': property}
    )