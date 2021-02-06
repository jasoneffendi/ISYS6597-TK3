from django.conf import settings
from django.http import HttpResponse
from django.db import connection
# from django.shortcuts import get_object_or_404
# from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK
)
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from api.permissions import AllowAny


class ReportingViewset(viewsets.ViewSet):

    @action(methods=['get'], detail=False, url_path='order-dev')
    def barang_dev(self, request):
        # TODO: Add Auth and Permissions
        # TODO: Move manual query a controller
        # Report of barang s_order, mean_order, s_demand, mean_deman
        # cv_order, cv_demand, BE, and lead time
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                core_barang.nama_barang,
                ROUND(STDDEV(jumlah_pesanan), 3) AS s_order,
                ROUND(
                    AVG(core_pemesanan.jumlah_pesanan),
                    3
                ) AS mean_order,
                ROUND(STDDEV(jumlah_produksi), 3) AS s_demand,
                ROUND(
                    AVG(core_produksi.jumlah_produksi),
                    3
                ) AS mean_demand,
                ROUND(
                    (
                        STDDEV(jumlah_pesanan) / AVG(jumlah_pesanan)
                    ),
                    3
                ) AS cv_order,
                ROUND(
                    (
                        STDDEV(jumlah_produksi) / AVG(jumlah_produksi)
                    ),
                    3
                ) AS cv_demand,
                ROUND(
                    (
                        (
                            STDDEV(jumlah_pesanan) / AVG(jumlah_pesanan)
                        ) / (
                            STDDEV(jumlah_produksi) / AVG(jumlah_produksi)
                        )
                    ),
                    3
                ) AS BE,
                core_produksi.lead_time,
                ROUND(
                    (
                        1 + ((2 * core_produksi.lead_time) / 30) + (
                            (2 * core_produksi.lead_time ^ 2) / (30 ^ 2)
                        )
                    ),
                    3
                ) AS parameter,
                ROUND(
                    (
                        (
                            STDDEV(jumlah_pesanan) / AVG(jumlah_pesanan)
                        ) / (
                            STDDEV(jumlah_produksi) / AVG(jumlah_produksi)
                        )
                    ) > 1 + ((2 * core_produksi.lead_time) / 30) + (
                        (2 * core_produksi.lead_time ^ 2) / (30 ^ 2)
                    ),
                    3
                ) AS Bullwhip_Effect
                FROM
                    core_barang
                INNER JOIN core_pemesanan ON core_pemesanan.barang_id = core_barang.id
                INNER JOIN core_produksi ON core_produksi.barang_id = core_pemesanan.barang_id
                GROUP BY
                    core_barang.nama_barang, core_produksi.lead_time;
            """)
            mapped_res = []
            for row in cursor:
                mapped_res.append({
                    'nama_barang': row[0],
                    's_order': row[1],
                    'mean_order': row[2],
                    's_demand': row[3],
                    'mean_demand': row[4],
                    'cv_order': row[5],
                    'cv_demand': row[6]
                })

            return Response({
                "data": mapped_res,
                "message": "Success"
            }, HTTP_200_OK)

        return Response({
            "data": [],
            "message": "Error"
        }, HTTP_200_OK)
