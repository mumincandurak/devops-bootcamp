mumincan@mumincan:~/devops-bootcamp/network$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host proto kernel_lo 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:48:78:b6 brd ff:ff:ff:ff:ff:ff
    altname enx00155d4878b6
    inet 172.26.182.54/20 brd 172.26.191.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe48:78b6/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
//This outputs show me my ip address and my interface

mumincan@mumincan:~/devops-bootcamp/network$ ip route
default via 172.26.176.1 dev eth0 proto kernel 
172.26.176.0/20 dev eth0 proto kernel scope link src 172.26.182.54 
//This output show me the my using gateway

mumincan@mumincan:~/devops-bootcamp/network$ sudo ss -tulnp
[sudo: authenticate] Password:       
Netid       State        Recv-Q       Send-Q                Local Address:Port                Peer Address:Port       Process                                         
udp         UNCONN       0            0                        127.0.0.54:53                       0.0.0.0:*           users:(("systemd-resolve",pid=78,fd=18))       
udp         UNCONN       0            0                     127.0.0.53%lo:53                       0.0.0.0:*           users:(("systemd-resolve",pid=78,fd=16))       
udp         UNCONN       0            0                    10.255.255.254:53                       0.0.0.0:*                                                          
udp         UNCONN       0            0                         127.0.0.1:323                      0.0.0.0:*           users:(("chronyd",pid=243,fd=4))               
udp         UNCONN       0            0                         127.0.0.1:323                      0.0.0.0:*                                                          
udp         UNCONN       0            0                             [::1]:323                         [::]:*                                                          
udp         UNCONN       0            0                             [::1]:323                         [::]:*           users:(("chronyd",pid=243,fd=5))               
tcp         LISTEN       0            4096                  127.0.0.53%lo:53                       0.0.0.0:*           users:(("systemd-resolve",pid=78,fd=17))       
tcp         LISTEN       0            1000                 10.255.255.254:53                       0.0.0.0:*                                                          
tcp         LISTEN       0            511                       127.0.0.1:36237                    0.0.0.0:*           users:(("MainThread",pid=556,fd=22))           
tcp         LISTEN       0            511                       127.0.0.1:46349                    0.0.0.0:*           users:(("MainThread",pid=622,fd=29))           
tcp         LISTEN       0            4096                     127.0.0.54:53                       0.0.0.0:*           users:(("systemd-resolve",pid=78,fd=19))       
//This outputs show me my ports and their status.

mumincan@mumincan:~/devops-bootcamp/network$ dig githup.com

; <<>> DiG 9.20.18-1ubuntu2.1-Ubuntu <<>> githup.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11394
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;githup.com.                    IN      A

;; ANSWER SECTION:
githup.com.             600     IN      A       212.32.254.35

;; Query time: 167 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Fri Jul 31 16:46:45 +03 2026
;; MSG SIZE  rcvd: 55
//This outputs show me number of recived ip.

mumincan@mumincan:~/devops-bootcamp/network$ traceroute github.com
traceroute to github.com (140.82.121.4), 30 hops max, 60 byte packets
 1  mumincan.mshome.net (172.26.176.1)  0.463 ms  0.642 ms  0.516 ms
 2  192.168.1.1 (192.168.1.1)  8.530 ms  8.587 ms  8.583 ms
 3  10.81.240.1 (10.81.240.1)  13.727 ms  13.722 ms  13.716 ms
 4  81.212.72.101.static.turktelekom.com.tr (81.212.72.101)  11.671 ms  10.390 ms  10.385 ms
 5  01-karsiyaka-sr7s-t2-2---51-nigde-sr2s-t3-1.statik.turktelekom.com.tr (81.212.208.226)  11.670 ms  13.694 ms  13.690 ms
 6  * * *
 7  * * *
 8  302-ams-col-2---34-ebgp-acibadem-sr12e-k.statik.turktelekom.com.tr (212.156.102.38)  76.093 ms  73.402 ms  73.361 ms
 9  et5-100.r4-ams1-nl.as5405.net (80.249.213.216)  73.827 ms  74.680 ms  75.626 ms
10  r5-fra3-de.as5405.net (94.103.180.89)  80.463 ms  79.721 ms  81.530 ms
11  r3-fra3-de.as5405.net (94.103.180.54)  81.535 ms  80.395 ms  81.791 ms
12  r2-fra3-de.as5405.net (94.103.180.53)  81.744 ms  81.397 ms  79.848 ms
13  45.153.82.39 (45.153.82.39)  87.265 ms  83.100 ms 45.153.82.37 (45.153.82.37)  79.945 ms
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
//This outputs show me the route of my request. My request visit 11 address and 19 empty address.

mumincan@mumincan:~/devops-bootcamp/network$ curl -I https://github.com
HTTP/2 200 
date: Fri, 31 Jul 2026 13:47:40 GMT
content-type: text/html; charset=utf-8
content-language: en-US
vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, X-Requested-With, X-GitHub-Client-Version, Accept-Language, Sec-Fetch-Site,Accept-Encoding, Accept, X-Requested-With
etag: W/"361331204557e1da795c9a7130ea6ba6"
cache-control: max-age=0, private, must-revalidate
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 0
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
content-security-policy: default-src 'none'; base-uri 'self'; child-src github.githubassets.com github.com/assets-cdn/worker/ github.com/assets/ gist.github.com/assets-cdn/worker/; connect-src 'self' uploads.github.com www.githubstatus.com collector.github.com raw.githubusercontent.com api.github.com github-cloud.s3.amazonaws.comgithub-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com *.rel.tunnels.api.visualstudio.com wss://*.rel.tunnels.api.visualstudio.com github.githubassets.com objects-origin.githubusercontent.com copilot-proxy.githubusercontent.com proxy.individual.githubcopilot.com proxy.business.githubcopilot.com proxy.enterprise.githubcopilot.com *.actions.githubusercontent.com wss://*.actions.githubusercontent.com productionresultssa0.blob.core.windows.net productionresultssa1.blob.core.windows.net productionresultssa2.blob.core.windows.net productionresultssa3.blob.core.windows.net productionresultssa4.blob.core.windows.net productionresultssa5.blob.core.windows.net productionresultssa6.blob.core.windows.net productionresultssa7.blob.core.windows.net productionresultssa8.blob.core.windows.net productionresultssa9.blob.core.windows.net productionresultssa10.blob.core.windows.net productionresultssa11.blob.core.windows.net productionresultssa12.blob.core.windows.net productionresultssa13.blob.core.windows.net productionresultssa14.blob.core.windows.net productionresultssa15.blob.core.windows.net productionresultssa16.blob.core.windows.net productionresultssa17.blob.core.windows.net productionresultssa18.blob.core.windows.net productionresultssa19.blob.core.windows.net github-production-repository-image-32fea6.s3.amazonaws.com github-production-release-asset-2e65be.s3.amazonaws.com insights.github.com wss://alive.github.com wss://alive-staging.github.com api.githubcopilot.com api.individual.githubcopilot.com api.business.githubcopilot.com api.enterprise.githubcopilot.com wss://production-copilot-host.webpubsub.azure.com edge.fullstory.com rs.fullstory.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com copilot-workspace.githubnext.com objects-origin.githubusercontent.com; frame-ancestors 'none'; frame-src viewscreen.githubusercontent.com notebooks.githubusercontent.com www.youtube-nocookie.com; img-src 'self' data: blob: github.githubassets.com media.githubusercontent.com camo.githubusercontent.com identicons.github.com avatars.githubusercontent.com private-avatars.githubusercontent.com github-cloud.s3.amazonaws.com objects.githubusercontent.com release-assets.githubusercontent.com secured-user-images.githubusercontent.com user-images.githubusercontent.com private-user-images.githubusercontent.com opengraph.githubassets.com repository-images.githubusercontent.com marketplace-screenshots.githubusercontent.com copilotprodattachments.blob.core.windows.net/github-production-copilot-attachments/ github-production-user-asset-6210df.s3.amazonaws.com customer-stories-feed.github.com spotlights-feed.github.com explore-feed.github.com objects-origin.githubusercontent.com *.githubusercontent.com images.ctfassets.net/8aevphvgewt8/; manifest-src 'self'; media-src github.com user-images.githubusercontent.com secured-user-images.githubusercontent.com private-user-images.githubusercontent.com github-production-user-asset-6210df.s3.amazonaws.com gist.github.com github.githubassets.com assets.ctfassets.net/8aevphvgewt8/ videos.ctfassets.net/8aevphvgewt8/; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; upgrade-insecure-requests; worker-src github.githubassets.com github.com/assets-cdn/worker/ github.com/assets/ gist.github.com/assets-cdn/worker/
server: github.com
accept-ranges: bytes
set-cookie: _gh_sess=GN%2BFKcXpR3udJhbAirKakpboYnZKbKSerQDDMHOEfCF%2FwaCw9JJiI%2BzkVUdcESDeIDpgBXvzzW%2FgKRj7VwRmZYQxef0FPRK6DwlKUjoYY%2FDFSEJBS%2BhNu25GyLL1WaHEuxUVSUxVEhOxGhNoCn61o5fKjNc%2BcBTVOYhXwVCBk3OEmf8Sn4MryaZmbnR%2F8Yt9G7xvmzSzy%2BIFOAJHW2uJkM7vv2vU50Q1DqROHCQ5q7njtqa2%2FffMZwIdBeNE0IpvaXiRc%2FRFeDnwzpSolLYNEA%3D%3D--AXo8FjamCygX6IHa--Npv8bXdJo6l1%2Ftpsw0II6w%3D%3D; path=/; HttpOnly; secure; SameSite=Lax
set-cookie: _octo=GH1.1.1610131577.1785505665; expires=Sat, 31 Jul 2027 13:47:45 GMT; domain=.github.com; path=/; secure; SameSite=Lax
set-cookie: logged_in=no; expires=Sat, 31 Jul 2027 13:47:45 GMT; domain=.github.com; path=/; HttpOnly; secure; SameSite=Lax
x-github-request-id: 4944:34A6D4:36C1C59:2B7CE46:6A6CA780
x-github-edge-region: fra
//This outputs show me the status of my request.
