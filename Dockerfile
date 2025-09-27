FROM odoo:14

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG=C.UTF-8

# Switch to root to install extra system dependencies
USER root

# Use Debian archive repos (buster is EOL)
RUN sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i '/security.debian.org/d' /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security buster/updates main" >> /etc/apt/sources.list && \
    apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y --no-install-recommends \
        fonts-noto-cjk \
        node-less \
        npm \
        python3-num2words \
        python3-pdfminer \
        python3-phonenumbers \
        python3-qrcode \
        python3-renderpm \
        python3-slugify \
        python3-vobject \
        python3-watchdog \
        python3-xlrd \
        python3-xlwt \
    && rm -rf /var/lib/apt/lists/*

# Install rtlcss globally (needed for RTL languages like Hebrew)
RUN npm install -g rtlcss

# Install Python debugger
RUN pip3 install -U debugpy

# Copy entrypoint script and Odoo configuration
COPY ./entrypoint.sh /
RUN sed -i 's/\r$//' /entrypoint.sh && chmod +x /entrypoint.sh
COPY ./odoo.conf /etc/odoo/

# Set permissions and addons volume
RUN chown odoo /etc/odoo/odoo.conf \
    && mkdir -p /mnt/extra-addons \
    && chown -R odoo /mnt/extra-addons

# Uncomment next line for production image to include custom addons
# COPY ./hebrew_learning /mnt/extra-addons    

VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose Odoo ports
EXPOSE 8069 8071 8072

# Default config file
ENV ODOO_RC=/etc/odoo/odoo.conf

# Helper script for waiting on PostgreSQL
COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Switch back to odoo user
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]