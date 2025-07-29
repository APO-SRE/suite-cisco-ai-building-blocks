from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_entry_ip_trusted_body import UpdateEntryIpTrustedBody
from ...models.update_entry_ip_trusted_response_400 import UpdateEntryIpTrustedResponse400
from ...models.update_entry_ip_trusted_response_401 import UpdateEntryIpTrustedResponse401
from ...models.update_entry_ip_trusted_response_403 import UpdateEntryIpTrustedResponse403
from ...models.update_entry_ip_trusted_response_404 import UpdateEntryIpTrustedResponse404
from ...models.update_entry_ip_trusted_response_500 import UpdateEntryIpTrustedResponse500
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateEntryIpTrustedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/ip/trusted/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        UpdateEntryIpTrustedResponse400,
        UpdateEntryIpTrustedResponse401,
        UpdateEntryIpTrustedResponse403,
        UpdateEntryIpTrustedResponse404,
        UpdateEntryIpTrustedResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = UpdateEntryIpTrustedResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = UpdateEntryIpTrustedResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = UpdateEntryIpTrustedResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = UpdateEntryIpTrustedResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = UpdateEntryIpTrustedResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Any,
        UpdateEntryIpTrustedResponse400,
        UpdateEntryIpTrustedResponse401,
        UpdateEntryIpTrustedResponse403,
        UpdateEntryIpTrustedResponse404,
        UpdateEntryIpTrustedResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpTrustedBody,
) -> Response[
    Union[
        Any,
        UpdateEntryIpTrustedResponse400,
        UpdateEntryIpTrustedResponse401,
        UpdateEntryIpTrustedResponse403,
        UpdateEntryIpTrustedResponse404,
        UpdateEntryIpTrustedResponse500,
    ]
]:
    """Update IP Trusted by ID

     Update the name, ip address, categories, and short description for the trusted IP feed.

    Args:
        id (str):
        body (UpdateEntryIpTrustedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateEntryIpTrustedResponse400, UpdateEntryIpTrustedResponse401, UpdateEntryIpTrustedResponse403, UpdateEntryIpTrustedResponse404, UpdateEntryIpTrustedResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpTrustedBody,
) -> Optional[
    Union[
        Any,
        UpdateEntryIpTrustedResponse400,
        UpdateEntryIpTrustedResponse401,
        UpdateEntryIpTrustedResponse403,
        UpdateEntryIpTrustedResponse404,
        UpdateEntryIpTrustedResponse500,
    ]
]:
    """Update IP Trusted by ID

     Update the name, ip address, categories, and short description for the trusted IP feed.

    Args:
        id (str):
        body (UpdateEntryIpTrustedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateEntryIpTrustedResponse400, UpdateEntryIpTrustedResponse401, UpdateEntryIpTrustedResponse403, UpdateEntryIpTrustedResponse404, UpdateEntryIpTrustedResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpTrustedBody,
) -> Response[
    Union[
        Any,
        UpdateEntryIpTrustedResponse400,
        UpdateEntryIpTrustedResponse401,
        UpdateEntryIpTrustedResponse403,
        UpdateEntryIpTrustedResponse404,
        UpdateEntryIpTrustedResponse500,
    ]
]:
    """Update IP Trusted by ID

     Update the name, ip address, categories, and short description for the trusted IP feed.

    Args:
        id (str):
        body (UpdateEntryIpTrustedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateEntryIpTrustedResponse400, UpdateEntryIpTrustedResponse401, UpdateEntryIpTrustedResponse403, UpdateEntryIpTrustedResponse404, UpdateEntryIpTrustedResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpTrustedBody,
) -> Optional[
    Union[
        Any,
        UpdateEntryIpTrustedResponse400,
        UpdateEntryIpTrustedResponse401,
        UpdateEntryIpTrustedResponse403,
        UpdateEntryIpTrustedResponse404,
        UpdateEntryIpTrustedResponse500,
    ]
]:
    """Update IP Trusted by ID

     Update the name, ip address, categories, and short description for the trusted IP feed.

    Args:
        id (str):
        body (UpdateEntryIpTrustedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateEntryIpTrustedResponse400, UpdateEntryIpTrustedResponse401, UpdateEntryIpTrustedResponse403, UpdateEntryIpTrustedResponse404, UpdateEntryIpTrustedResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
